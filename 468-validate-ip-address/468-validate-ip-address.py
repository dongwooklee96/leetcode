class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        IPV4 = '(\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])'
        
        ipv4 = \
            re.compile(r'^({p}\.){{3}}{p}$'.format(p=IPV4))
        if ipv4.match(queryIP):
            return "IPv4"
        
        IPV6 = '([0-9a-f]{1,4})'
        
        ipv6 = \
            re.compile(r'^({p}\:){{7}}{p}$'.format(p=IPV6), re.IGNORECASE)
        
        if ipv6.match(queryIP):
            return "IPv6"
        
        return "Neither"
        