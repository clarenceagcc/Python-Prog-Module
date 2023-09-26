import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv

url_list = ["https://legacy.vault.com/industries-professions/professions/s/software-designers",
            "https://legacy.vault.com/industries-professions/professions/i/information-security-analysts",
            "https://legacy.vault.com/industries-professions/professions/c/computer-systems-programmer-analysts",
            "https://legacy.vault.com/industries-professions/professions/s/site-reliability-engineers",
            "https://legacy.vault.com/industries-professions/professions/s/software-engineers",
            "https://legacy.vault.com/industries-professions/professions/d/data-scientists",
            "https://legacy.vault.com/industries-professions/professions/m/machine-learning-engineers",
            "https://legacy.vault.com/industries-professions/professions/i/information-technology-project-managers",
            "https://legacy.vault.com/industries-professions/professions/a/agile-coaches-or-trainers",
            "https://legacy.vault.com/industries-professions/professions/a/artificial-intelligence-specialists",
            "https://legacy.vault.com/industries-professions/professions/a/augmented-reality-developers",
            "https://legacy.vault.com/industries-professions/professions/a/automation-engineers",
            "https://legacy.vault.com/industries-professions/professions/b/back-end-developers",
            "https://legacy.vault.com/industries-professions/professions/b/big-data-developers",
            "https://legacy.vault.com/industries-professions/professions/b/biometrics-systems-specialists",
            "https://legacy.vault.com/industries-professions/professions/b/blockchain-developers",
            "https://legacy.vault.com/industries-professions/professions/c/chief-information-officers",
            "https://legacy.vault.com/industries-professions/professions/c/chief-information-security-officers",
            "https://legacy.vault.com/industries-professions/professions/c/clinical-data-managers",
            "https://legacy.vault.com/industries-professions/professions/c/cloud-engineers",
            "https://legacy.vault.com/industries-professions/professions/c/computer-and-office-machine-service-technicians",
            "https://legacy.vault.com/industries-professions/professions/c/computer-network-administrators",
            "https://legacy.vault.com/industries-professions/professions/c/computer-programmers",
            "https://legacy.vault.com/industries-professions/professions/c/computer-support-service-owners",
            "https://legacy.vault.com/industries-professions/professions/c/computer-support-specialists",
            "https://legacy.vault.com/industries-professions/professions/c/computer-trainers",
            "https://legacy.vault.com/industries-professions/professions/c/cryptocurrency-specialists",
            "https://legacy.vault.com/industries-professions/professions/c/customer-success-managers",
            "https://legacy.vault.com/industries-professions/professions/c/cybersecurity-architects",
            "https://legacy.vault.com/industries-professions/professions/d/data-processing-technicians",
            "https://legacy.vault.com/industries-professions/professions/d/data-warehousing-specialists",
            "https://legacy.vault.com/industries-professions/professions/d/database-specialists",
            "https://legacy.vault.com/industries-professions/professions/d/deepfake-professionals",
            "https://legacy.vault.com/industries-professions/professions/d/digital-agents",
            "https://legacy.vault.com/industries-professions/professions/d/digital-workplace-experience-engineers",
            "https://legacy.vault.com/industries-professions/professions/d/document-management-specialists",
            "https://legacy.vault.com/industries-professions/professions/e/electrical-engineering-technologists",
            "https://legacy.vault.com/industries-professions/professions/e/electrical-engineers",
            "https://legacy.vault.com/industries-professions/professions/e/electronics-engineering-technicians",
            "https://legacy.vault.com/industries-professions/professions/e/electronics-engineers",
            "https://legacy.vault.com/industries-professions/professions/e/electronics-service-technicians",
            "https://legacy.vault.com/industries-professions/professions/e/embedded-systems-engineers",
            "https://legacy.vault.com/industries-professions/professions/e/enterprise-architects",
            "https://legacy.vault.com/industries-professions/professions/e/etl-developers",
            "https://legacy.vault.com/industries-professions/professions/f/fiber-optics-technicians",
            "https://legacy.vault.com/industries-professions/professions/f/full-stack-developers-engineers",
            "https://legacy.vault.com/industries-professions/professions/f/futurists",
            "https://legacy.vault.com/industries-professions/professions/g/geospatial-analytics-specialists",
            "https://legacy.vault.com/industries-professions/professions/g/graphic-designers",
            "https://legacy.vault.com/industries-professions/professions/g/graphics-programmers",
            "https://legacy.vault.com/industries-professions/professions/h/hardware-engineers",
            "https://legacy.vault.com/industries-professions/professions/h/health-informaticists",
            "https://legacy.vault.com/industries-professions/professions/i/information-assurance-analysts",
            "https://legacy.vault.com/industries-professions/professions/i/information-technology-consultants",
            "https://legacy.vault.com/industries-professions/professions/i/information-technology-infrastructure-engineers",
            "https://legacy.vault.com/industries-professions/professions/i/internet-consultants",
            "https://legacy.vault.com/industries-professions/professions/i/internet-of-things-developers",
            "https://legacy.vault.com/industries-professions/professions/j/javascript-developers",
            "https://legacy.vault.com/industries-professions/professions/m/microelectronics-technicians",
            "https://legacy.vault.com/industries-professions/professions/m/mathematicians",
            "https://legacy.vault.com/industries-professions/professions/m/model-view-controller-developers",
            "https://legacy.vault.com/industries-professions/professions/n/network-operations-center-engineers",
            "https://legacy.vault.com/industries-professions/professions/n/network-operations-center-technicians",
            "https://legacy.vault.com/industries-professions/professions/o/online-gambling-specialists",
            "https://legacy.vault.com/industries-professions/professions/p/personal-privacy-advisors",
            "https://legacy.vault.com/industries-professions/professions/p/product-owners",
            "https://legacy.vault.com/industries-professions/professions/p/project-managers",
            "https://legacy.vault.com/industries-professions/professions/s/scrum-masters",
            "https://legacy.vault.com/industries-professions/professions/s/semiconductor-technicians",
            "https://legacy.vault.com/industries-professions/professions/s/software-application-developers",
            "https://legacy.vault.com/industries-professions/professions/s/software-quality-assurance-testers",
            "https://legacy.vault.com/industries-professions/professions/s/solutions-architects",
            "https://legacy.vault.com/industries-professions/professions/s/systems-setup-specialists",
            "https://legacy.vault.com/industries-professions/professions/t/technical-support-specialists",
            "https://legacy.vault.com/industries-professions/professions/t/technical-writers-and-editors",
            "https://legacy.vault.com/industries-professions/professions/t/technology-ethicists",
            "https://legacy.vault.com/industries-professions/professions/w/wireless-service-technicians"]

# setting up Excel file
# change profession name each file

#file = open('vault_legacy_jobs.csv', 'w', newline='')
#writer = csv.writer(file)

# data parsing portion
jobs = []

for url in url_list:
    req = requests.get(url)

    soup = BeautifulSoup(req.content, "html.parser")

    # beautifying data - cooking soup and adding ingredients to excel

    # change profession name each url

    main_header = [soup.find('h1').text] # job title
    #header1 = ['Overview']

    #writer.writerow(main_header)
    #writer.writerow(header1)

    everything = soup.find('div', attrs={'class': 'd-flex flex-column w-100 contentBlock1 p-b-10 m-b-0'})

    # overview
    overview_main = everything.find('p')
    overview_main2 = [overview_main.text]
    overview_main_clean = [overview_main2[0].strip("\n").replace("\xa0", " ")] # job desc
    #writer.writerow(overview_main_clean)

    # insights
    insight_titles = ['Salary Range', 'Minimum Education Level', 'Certification/License', 'Outlook']
    #writer.writerow(insight_titles)

    insights = everything.find_all('strong')
    insights_clean = []
    for insight in insights:
        insights_clean.append(insight.text)

    for insight in insights_clean:
        if insight == " ":
            insights_clean.remove(insight)
        elif insight == "":
            insights_clean.remove(insight)

    #writer.writerow(insights_clean)

    # personality traits
    personality_title = ['Personality Traits']
    #writer.writerow(personality_title)

    personality_tab = everything.find('div', attrs={'class': 'd-flex flex-column justify-content-between align-items-center justify-content-lg-center group'})
    personality_specific = personality_tab.find_all('p')
    personality_traits = []
    for trait in personality_specific:
        personality_traits.append(trait.text)
    #writer.writerow(personality_traits)

    # career ladder
    ladder_title = ['Career Ladder']
    #writer.writerow(ladder_title)

    ladder_tab = everything.find('div', attrs={'class': 'd-flex flex-column align-items-center justify-content-start group w-100'})
    ladder_specific = [ladder_tab.find('div', attrs={'class': 'description'})] + ladder_tab.find_all('p')
    career_ladder = []
    for career in ladder_specific:
        career_ladder.append(career.text)
    career_ladder.reverse()
    #writer.writerow(career_ladder)

    #writer.writerow("")
