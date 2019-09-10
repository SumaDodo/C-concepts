class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        answer = collections.Counter()
        
        for domain in cpdomains:
            count, domain = domain.split()
            count = int(count)
            fragments = domain.split(".")
            for i in range(len(fragments)):
                answer[".".join(fragments[i:])] += count
                
        return ["{} {}".format(ct, dom) for dom,ct in answer.items()]
