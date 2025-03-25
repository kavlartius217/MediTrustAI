from crewai.flow import Flow, start, listen, and_, or_, router
from pydantic import BaseModel
from major_crew import Medic_Bot
from doctor_crew import Doctor_Bot
import nest_asyncio
nest_asyncio.apply()

class State(BaseModel):
  abnormalities:str=" "
  decision:str=" "


class MediTrustAI(Flow[State]):
  @start()
  def medic_bot(self):
    result=(
        Medic_Bot().crew().kickoff({"report":report})
    )
    self.state.abnormalities=result.raw

  @listen(medic_bot)
  def ask(self):
    decision=input("Would you like to have a list of recommended doctors")
    self.state.decision=decision

  @router(ask)
  def route(self):
    x=self.state.decision
    if(x=="yes"):
      return "Proceed"
    else:
      return "Dont Proceed"

  @listen("Proceed")
  def doctor_bot(self):
    result=(
        Doctor_Bot().crew().kickoff({"user_city":"Pune","abnormalities":self.state.abnormalities})
    )
