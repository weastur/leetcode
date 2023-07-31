class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        s = set()
        for email in emails:
            local_name, domain = email.split('@')
            local_name = local_name.replace('.', '')
            pos = local_name.find('+')
            if pos != -1: 
                local_name = local_name[:pos]
            s.add(f'{local_name}@{domain}')
        return len(s)