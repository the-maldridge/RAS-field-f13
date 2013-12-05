import logging
import time

class MatchTimer:
  def __init__(self):
    logging.debug("Loaded the system time library")
    self.running = False

  def startMatch(self):
    logging.info("Match started at %d", time.time())
    self.startTime = time.time()
    self.running = True

  def endMatch(self):
    logging.info("Match ended at %d", time.time())
    self.endTime = time.time()
    self.running = False

  def currentTime(self):
    if self.running:
      return float(time.time()-self.startTime)
    else:
      logging.error("Attempted to get time for non running match")
      return None

  def matchElapsed(self):
    logging.info("Match has ended with %d on the clock", self.endTime-self.startTime)
    return self.endTime-self.startTime

  def matchIsRunning(self):
    return self.running
