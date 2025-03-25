# **MediTrustAI - AI-Powered Medical Report Analysis & Doctor Recommendation System**

## **📌 Project Overview**
MediTrustAI is an advanced **agentic system** built using **CrewAI** to analyze blood reports, detect abnormalities, assign severity scores, and provide medical insights. If necessary, the system also recommends **specialist doctors** based on the detected health conditions.

## **🛠️ System Architecture**
MediTrustAI consists of **two main crews**, each handling a different part of the workflow:

### **🔹 Crew 1: Blood Report Analysis Crew** (Main Processing Unit)
Responsible for analyzing blood reports and identifying abnormalities.

#### **Agents in Crew 1:**
1️⃣ **Report Extraction Agent**  
   - Extracts medical parameters and their values from the uploaded blood report.

2️⃣ **Abnormalities Detection Agent**  
   - Identifies abnormal values and assigns a severity score (**Normal, Mild, Moderate, or Severe**).

3️⃣ **Medical Explanation Agent**  
   - Provides detailed insights into abnormal parameters, explaining their significance and possible health implications.

✅ **Next Step:** The system asks the user if they want a list of recommended doctors.

---

### **🔹 Crew 2: Doctor Recommendation Crew** (Triggered Only If Needed)
If the user requests a doctor recommendation, this crew searches for specialists based on severity and location.

#### **Agent in Crew 2:**
4️⃣ **Doctor Finder Agent**  
   - Finds top-rated doctors specializing in the detected abnormalities based on the user's location.
   - Uses live search tools (e.g., **SerperDevTool**) for real-time doctor listings.

✅ **Next Step:** If doctors are recommended, the system provides their details and consultation options.

---

## **🔄 Execution Flow**
1️⃣ **User uploads a blood report (PDF)**  
2️⃣ **Blood Report Analysis Crew extracts and processes the report:**
   - Extracts medical parameters.
   - Detects abnormalities and assigns severity.
   - Provides medical explanations.
3️⃣ **User is asked if they need doctor recommendations.**
   - If **yes**, it triggers the **Doctor Recommendation Crew**.
   - If **no**, the process ends.

## **🚀 Features & Benefits**
✅ **Automated blood report analysis**  
✅ **Severity scoring for abnormalities**  
✅ **Medical insights & explanations**  
✅ **Doctor recommendations based on severity & location**  
✅ **Integration with live search APIs for real-time doctor availability**  
✅ **Scalable & modular CrewAI implementation**  

## **🔧 Tech Stack**
- **Python** (Backend)
- **CrewAI** (Agentic System)
- **LangChain** (Medical Knowledge Retrieval)
- **PyPDFLoader** (Extracting blood report data)
- **SerperDevTool** (Fetching real-time doctor recommendations)
