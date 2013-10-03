import json
import logging
import sys

class db():
#-------------DB Management---------------------------

  def __init__(self, t3file):
    self.disk = t3file
    try:
      dataStore = open(t3file, 'w')
      logging.info("Attempting to load the database from disk")
      self.db = json.load(dataStore)
      logging.info("Successfully loaded database from disk")
    except:
      logging.error("Could not load database")
      sys.exit(1)
    finally:
      dataStore.close()

  def commitDB(self):
    try:
      dataStore = open(self.disk)
      logging.info("Attempting to save database to disk")
      json.dump(self.db, dataStore, indent=2)
      logging.info("Successfully dumped database to disk")
    except:
      logging.critical("Could not save database")
      logging.critical("Dumping database to log")
      logging.critical(json.dumps(self.db))
    finally:
      dataStore.close()
   

#-------------Team Management--------------------------

  def createTeam(self, teamName, teamNumber):
    if teamName in self.db:
      logging.error("Team %s exists!", teamName)
    else:
      logging.info("Added team %s", teamName)
      self.db[teamName][number] = teamNumber

  def delTeam(self, teamName):
    if teamName not in self.db:
      logging.error("Team %s does not exist, so can't delete", teamName)
    else:
      self.db[teamName] = None
      logging.info("Nullified %s", teamName)

  def listTeams(self):
    logging.info("Listed Teams")
    return list(self.db["teamName"])

#---------------Ranking-----------------------------------

def getRanks(self):
  logging.info("Ranked Teams")
  return self.db[][]

#-------------Penalties----------------------------------

  def assignPenalty(self, teamName, matchNum, penaltyType, timeAssigned):
     self.db[teamName]["matches"][matchNum]["penalties"] = {"type":penaltyType, "assignedTime":timeAssigned}
     logging.info("Assigned penalty %s to %s @ %d", penaltyType, teamName, timeAssigned)

  def removePenalty(self, teamName, matchNum, penaltyType, timeAssigned):
     self.db[teamName]["matches"][matchNum]["penalties"] = None
     logging.info("Removed penalty %s from %s @ %d", penaltyType, teamName, timeAssigned)
