import jsonrpc
import sys

try:
    local = jsonrpc.ServiceProxy("http://user:pass@127.0.0.1:18332/")
    print local.help()
 
    
except jsonrpc.proxy.JSONRPCException, e:
    print repr(e.error)
except:
    print "Unexpected error:", sys.exc_info()[0]
    raise