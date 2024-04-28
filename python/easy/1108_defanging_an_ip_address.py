# https://leetcode.com/problems/defanging-an-ip-address/
class Solution(object):
    def defangIPaddr(self, address):
        return address.replace(".", "[.]")
