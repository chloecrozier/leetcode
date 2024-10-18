# https://leetcode.com/problems/subdomain-visit-count/description/
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        ht = {}
        for ls in cpdomains:
            count, domains = ls.split(' ')
            domainList = []
            for subDomain in domains.split('.'):
                if not domainList:
                    domainList.append(subDomain)
                else:
                    for i in range(len(domainList)):
                        domainList[i] = domainList[i] + '.' + subDomain
                    domainList.append(subDomain)

            count = int(count)
            for domain in domainList:
                if domain in ht:
                    ht[domain] += count
                else:
                    ht[domain] = count
        return [f'{count} {domain}' for domain, count in ht.items()]
