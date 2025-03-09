import requests
import csv
import argparse
import re
import xml.etree.ElementTree as ET
from typing import List, Dict, Optional

# PubMed API Base URLs
PUBMED_API_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
PUBMED_FETCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"

def fetch_pubmed_ids(query: str) -> List[str]:
    """Fetch PubMed IDs matching the search query."""
    params = {
        "db": "pubmed",
        "term": query,
        "retmode": "json",
        "retmax": 10  # Limit results for now
    }
    response = requests.get(PUBMED_API_URL, params=params)
    response.raise_for_status()
    data = response.json()
    
    return data.get("esearchresult", {}).get("idlist", [])

def fetch_pubmed_details(pubmed_ids: List[str]) -> List[Dict[str, str]]:
    """Fetch details for given PubMed IDs."""
    if not pubmed_ids:
        return []
    
    params = {
        "db": "pubmed",
        "id": ",".join(pubmed_ids),
        "retmode": "xml"
    }
    response = requests.get(PUBMED_FETCH_URL, params=params)
    response.raise_for_status()
    
    return parse_pubmed_xml(response.text)

def parse_pubmed_xml(xml_data: str) -> List[Dict[str, str]]:
    """Parse XML response to extract required details."""
    root = ET.fromstring(xml_data)
    papers = []
    
    for article in root.findall(".//PubmedArticle"):
        pubmed_id = article.find(".//PMID").text if article.find(".//PMID") is not None else ""
        title = article.find(".//ArticleTitle").text if article.find(".//ArticleTitle") is not None else ""
        pub_date = article.find(".//PubDate/Year")
        publication_date = pub_date.text if pub_date is not None else ""
        
        authors = []
        corresponding_author_email = ""
        
        for author in article.findall(".//Author"):
            last_name = author.find("LastName")
            first_name = author.find("ForeName")
            affiliation = author.find("AffiliationInfo/Affiliation")
            email_match = re.search(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", affiliation.text if affiliation is not None else "")
            
            author_info = {
                "name": f"{first_name.text if first_name is not None else ''} {last_name.text if last_name is not None else ''}",
                "affiliation": affiliation.text if affiliation is not None else ""
            }
            authors.append(author_info)
            
            if email_match:
                corresponding_author_email = email_match.group(0)
        
        non_academic_authors = filter_non_academic_authors(authors)
        company_affiliations = [author["affiliation"] for author in non_academic_authors if is_company_affiliation(author["affiliation"])]
        
        papers.append({
            "PubmedID": pubmed_id,
            "Title": title,
            "Publication Date": publication_date,
            "Non-academic Authors": "; ".join(a["name"] for a in non_academic_authors),
            "Company Affiliations": "; ".join(company_affiliations),
            "Corresponding Author Email": corresponding_author_email
        })
    
    return papers

def filter_non_academic_authors(authors: List[Dict[str, str]]) -> List[Dict[str, str]]:
    """Identify non-academic authors based on heuristics."""
    return [author for author in authors if not re.search(r"university|institute|college|lab", author.get("affiliation", ""), re.IGNORECASE)]

def is_company_affiliation(affiliation: str) -> bool:
    """Check if an affiliation belongs to a pharmaceutical or biotech company."""
    return bool(re.search(r"pharma|biotech|Inc\.|LLC|Corp|Ltd", affiliation, re.IGNORECASE))

def save_to_csv(papers: List[Dict[str, str]], filename: Optional[str] = None):
    """Save the paper details to a CSV file or print to console."""
    fields = ["PubmedID", "Title", "Publication Date", "Non-academic Authors", "Company Affiliations", "Corresponding Author Email"]
    
    if filename:
        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=fields)
            writer.writeheader()
            writer.writerows(papers)
    else:
        print(",".join(fields))  # Print header
        for row in papers:
            print(",".join(str(row.get(field, "")) for field in fields))

def main():
    parser = argparse.ArgumentParser(description="Fetch research papers from PubMed")
    parser.add_argument("query", type=str, help="Search query")
    parser.add_argument("-f", "--file", type=str, help="Filename to save results", default=None)
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug mode")
    args = parser.parse_args()
    
    if args.debug:
        print(f"Fetching papers for query: {args.query}")
    
    pubmed_ids = fetch_pubmed_ids(args.query)
    
    if args.debug:
        print("PubMed IDs fetched:", pubmed_ids)
    
    papers = fetch_pubmed_details(pubmed_ids)
    
    if args.debug:
        print("Fetched papers:", papers)
    
    save_to_csv(papers, args.file)

if __name__ == "__main__":
    main()