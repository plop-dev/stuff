def timecommand():
    print('the time here')

def sayhi():
    print('say hi')

command_map = {
    "('what is'; or \"what's\";) and 'time';": lambda: timecommand(),
    "'hello'; and 'how are you';": lambda: sayhi(),
}
user_query = 'what is the game stormworks?'
for cmd, func in command_map.items():
    command = cmd.replace(';', ' in user_query')
    if eval(command):
        func()
        break
