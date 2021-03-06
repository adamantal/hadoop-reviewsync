import logging

LOG = logging.getLogger(__name__)


class ObjUtils:
  
  @staticmethod
  def print_properties(obj):
    LOG.info("Printing properties of obj: %s", obj)
    for property, value in vars(obj).iteritems():
      LOG.info("%s: %s", property, value)
