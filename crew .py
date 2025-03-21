from crewai import Agent, Task, Crew, Process
from crewai.project import agent, task, crew, CrewBase
from crewai import LLM
import yaml
import os

#report
from langchain_community.document_loaders import PyPDFLoader
report=PyPDFLoader('/content/WM17S.pdf')
report=report.load()
from langchain.text_splitter import RecursiveCharacterTextSplitter
rcts=RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
report=rcts.split_documents(report)
report= "\n\n".join([doc.page_content for doc in report])



llm=LLM(model="mixtral-8x7b-32768")

from crewai_tools import SerperDevTool

@CrewBase
class MediTrustAI():
  """This defines the intial screening as well as the generation part of the product"""
  agents_config="/content/agents.yaml"
  tasks_config="/content/tasks.yaml"

  @agent
  def blood_test_analyst(self)->Agent:
    return Agent(
      config=self.agents_config['blood_test_analyst'],
      memory=True,
      verbose=True,
      allow_delegation=True
    )

  @agent
  def health_researcher_agent(self)->Agent:
    return Agent(
      config=self.agents_config['health_researcher_agent'],
      function_calling_llm=llm,
      tools=[SerperDevTool()],
      memory=True,
      verbose=True,
      allow_delegation=True
    )

  @agent
  def health_advisor_agent(self)->Agent:
    return Agent(
      config=self.agents_config['health_advisor_agent'],
      memory=True,
      verbose=True,
      allow_delegation=True
    )

  @task
  def blood_test_task(self)->Task:
    return Task(
      config=self.tasks_config['blood_test_task']
    )

  @task
  def health_researcher_task(self)->Task:
    return Task(
      config=self.tasks_config['health_researcher_task']
    )

  @task
  def health_advisor_task(self)->Task:
    return Task(
      config=self.tasks_config['health_advisor_task']
    )

  @crew
  def crew(self)->Crew:
    return Crew(
      agents=[self.blood_test_analyst(),self.health_researcher_agent(),self.health_advisor_agent()],
      tasks=[self.blood_test_task(),self.health_researcher_task(),self.health_advisor_task()],
      process=Process.sequential
    )


m1=MediTrustAI()
result=m1.crew().kickoff({"blood_test_report":"report"})


