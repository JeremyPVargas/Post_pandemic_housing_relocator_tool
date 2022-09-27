<h1 style="text-align: center;">Project: Post Pandemic Housing Relocator Tool</h1>


<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#team-members">Team members</a>
    </li>
    <li>
      <a href="#project-description-outline">Project Description Outline</a>
    </li>
    <li>
      <a href="#research-questions-to-answer">Research questions to answer</a>
    </li>
    <li>
      <a href="#datasets-to-be-used">Datasets to be used</a>
    </li>
    <li>
      <a href="#rough-breakdown-of-tasks">Rough breakdown of tasks</a>
    </li>
      <ul>
        <li><a href="#phase-1-concept">Phase 1: Concept</a></li>
        <li><a href="#phase-2-design">Phase 2: Design</a></li>
        <li><a href="#phase-3-iteration">Phase 3: Iteration</a></li>
        <li><a href="#phase-4-release">Phase 4: Release </a></li>
        <li><a href="#phase-5-track-and-monitor">Phase 5: Track and Monitor</a></li>
      </ul>
    </li>
  </details>

<!--Team members -->
## **Team members:**

| Name            | Email                     | Github Alias                       |
|:----------------|:-------------------------:|----------------------------------|
| Cuong Ha       | *cuong.ha@gmail.com*       | <a href="#<https://github.com/chh52>">CHH52</a>         |
| Saidee Padilla |  *rosario050597@gmail.com* | <a href="#<https://github.com/saideepadilla>">Saideepadilla</a> |
| Jeremy Vagas   |  *jeremypvargas@gmail.com* | <a href="#<https://github.com/JeremyPVargas>">JeremyPVargas</a>



____

<!--Project Description Outline-->
## **Project Description Outline**
>The scope of this project is to develop a tool that provides the user with real-time US rental market data; which the user can utilize to evaluate moving options in a Post-Pandemic economy. 
The app will provide information such as number of properties available, rental prices, property types, etc. As an output, the app will produce a report of data pulled into CSV file.

____

<!--Research questions to answer -->
## **Research questions to answer**
Technical requirements:
-	Hosting: GitHub
-	Languages: 
  - Python (libraries and dependencies)
  - SQL
  - HTML
  - Markdown 
-	API: Yes
-	Web: Yes (several sites and data sources identified)
- CUI: Yes
- Export to file: Yes to CSV

User
- User interacts with application by selecting from a list of cities available in a menu
- Application returns the number of units availabe for rent and provides rental options
- User selects if reported data needs to be saved to a CSV file

Additional Features - Possible future iterations
> Depending on time and data availability the application may also query, extract, and cross reference additional demographic and economic data for the city selected such as: 
  - Cost of living
  - Fortune 500 or 1000 jobs available per industry for the city selected

____

<!--Datasets to be used-->
## Datasets to be used
><a href="#<https://craigslist.com>">Craigslist.com</a>
>>About: Craiglists contains vast market rental & housing data available.
>>Status: Tested data parsing and extraction.
>>Risk 1: Data needs to be cleaned multiple times.
>>Risk 2: Each Metropolitan or City would have to be queried, it is uknonw if each city has the same data strutural frame design.

><a href="#<https://zillow.com>">Zillow.com</a>
>>API isn needed and Rapid API is available with a paid subscription service
>>If used, there is a cost per API request, which can become in cost prohibitive based on the requirements for this academic project.

><a href="#<https://apartments.com>">Apartments.com</a>
>>Status: Pending API access approval
>>Ideally, this would be the preferred data source

><a href="#<https://www.apartmentlist.com/research/category/data-rent-estimate>">Apartmentlists.com</a>
>>About: Data includes city-level historical estimates (2017 – Present).  Data is through August 2022 and includes median rental prices for 1br and 2br.  CSV
>>Status: Pending data quality review.
>>Risk: data is not recent. Data is through August 2022 and includes median rental prices for 1br and 2br.  Data presented is on CSV format. 

><a href="#https://www.rent.com/research/average-rent-price-report/>">Rent.com</a>
>>About: large data set and market leader for rental properties.
>>Status: Need API, and explore extraction feasibility. Table we’d need to copy paste and format into a usable format.  City level data for 1br and 2br by city
>>Risk: Feasibility contraints.

><a href="#https://www.huduser.gov/portal/datasets/fmr.html#2022_data>">HUD.gov</a>
>>About: Gov data source. 
>>Status: Pending data quality review. Need to look at what is considered “Fair Market Rates”. Data available by zip code
>>Risk: Unknown data quality, by zipcode, not city. Would have to cross reference by city if data source is selected.

><a href="#https://www.numbeo.com/cost-of-living/comparison.jsp>">Numbeo.com</a>
>>About: Cost of living website
>>Status: Pending data quality review, and feasibility of extraction
>>Risk: Adding out of scope complexity if selected. Preferred use for feature post initial release. 

____

<!--Rough breakdown of tasks-->
## Rough breakdown of tasks
This project will follow the AGILE methodology for application develoment. A standard approach follows this outline:

<!--Phase 1: Concept-->
### **Phase 1: Concept**
- 1.1 Assemble team
  - 1.1.1 Complete stakeholder analysis
- 1.2 Explore application options
  - 1.2.1 Complete use case scenarios
  - 1.2.2 Review application criteria
  - 1.2.3 Survey application options
  - 1.2.3 Evaluate capabilities and risks
- 1.3 Define Scope
- 1.4 Create WBS
- 1.5 Complete Project Proposal
- 1.6 Request sponsor approval
- 1.7 Modify project plan based on sponsor feedback
- 1.8 Document approval and close phase

<!--Phase 2: Design-->
### **Phase 2: Design**
- 2.1 Gather data sources
  - 2.1.1 Evaluate data sources
  - 2.1.2 Obtain APIs
  - 2.1.3 Validate data available
  - 2.1.4 Develop queries to pull data for analysis
  - 2.1.5 Review and analyze data quality
- 2.2 Application Design
  - 2.2.1 Complete design whiteboarding session
  - 2.2.2 Document story board
  - 2.2.3 Develop application conceptual model
  - 2.2.4 Review application modular design
  - 2.2.5 Evaluate risks
- 2.3 Application Modules
  - 2.3.1 Data Modules
  - 2.3.2 CLI Interface
  - 2.3.3 Resources
- 2.3 Application Data Model
  - 2.3.1 Format and clean data
  - 2.3.3 Determine data structure
  - 2.3.2 Develop data frame
- 2.4 Request sponsor approval
- 2.5 Monitor and document project version control

<!--Phase 3: Iteration-->
### **Phase 3: Iteration**
Develop query and conections from interface to data sources
- 3.1 Iteraion 1
  - 3.1.1 Print 1
    - 3.1.1.1 Data Module
    - 3.1.1.2 Modular interface
    - 3.1.1.3 Stand up 1
    - Review progress
    - Test 1
- 3.2 Iteraion 2
  - 3.2.1 Sprint 2
  - 3.2.2 Stand up 2
- 3.3 Repeat iterations
- 3.4 Review time constraints
- 3.5 Test connections
- 3.6 Monitor version control

<!--Phase 4: Release-->
### **Phase 4: Release**
- 4.1 Gain sponsor approval
- 4.2 Complete version control documentation
- 4.3 Commit final version
- 4.4 Submit code for sponsor review
- 4.5 Complete Lessons Learned
- 4.6 Complete Project Close Activities

<!--Phase 5: Track and monitor-->
### **Phase 5: Track and monitor**
- 5.1 Gater user feedback
- 5.2 Create review cadance
- 5.3 Document feature requets
- 5.4 Plan feature updates
- 5.5 Run Iterations




