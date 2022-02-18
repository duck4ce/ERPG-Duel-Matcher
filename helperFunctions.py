class HelperFunctions:
  def __init__(self):
        pass
    
  @classmethod
  def getLocalQueue(queue_list, guild):
    return dict(queue_list)[message.guild]