from Game import Game
from Agent import Agent



COLORS = {
    '1': '🟥',
    '2': '🟦',
    '3': '🟨',
    '4': '🟪',
    '5': '🟩',
    '6': '🟫',
    '7': '⬛',
}

agents: list[Agent] = []
games: list[Game] = []

def printHeader(title):
    print("\n" + "=" * 40)
    print(f" {title.center(36)} ")
    print("=" * 40)

def selectAgent(prompt) -> Agent:
    printHeader("AVAILABLE AGENTS")
    for idx, agent in enumerate(agents, 1):
        print(f"[{idx}] {agent.username} ({agent.color}) {'(Bot)' if agent.isBot else ''}")
    while True:
        try:
            choice = int(input(prompt))
            if 1 <= choice <= len(agents):
                return agents[choice-1]
            print("Invalid agent selection!")
        except ValueError:
            print("Please enter a number!")

while True:
    try:
        printHeader("MAIN MENU")
        userInput = int(input(
            "[1] Create New Agent\n"
            "[2] Create New Game\n"
            "[3] Play Existing Game\n"
            "[4] Exit\n"
            "Input => "
        ))
    except ValueError:
        print("Invalid input! Please enter a number between 1-4.")
        continue
    match userInput:
        case 1:
            printHeader("CREATE NEW AGENT")
            username = input("Enter Agent's username: ").strip()
            if not username:
                print("Username cannot be empty!")
                continue
            while True:
                colorChoice = input(
                    "Choose color:\n"
                    "[1] Red 🟥\n"
                    "[2] Blue 🟦\n"
                    "[3] Yellow 🟨\n"
                    "[4] Purple 🟪\n"
                    "[5] Green 🟩\n"
                    "[6] Brown 🟫\n"
                    "[7] Black ⬛\n"
                    "Input => "
                )
                if colorChoice in COLORS:
                    color = COLORS[colorChoice]
                    break
                print("Invalid color choice! Please select 1-4.")
            while True:
                botChoice = input("Make This Agent A Bot? \n[1] Yes \n[2] No\nInput => ")
                if botChoice in ('1', '2'):
                    isBot = botChoice == '1'
                    break
                print("Invalid Choice! Please Select 1 or 2.")
            agents.append(Agent(username, color, isBot))
            print(f"\nAgent '{username}' Created Successfully!")
        case 2:
            printHeader("CREATE NEW GAME")
            gameName = input("Enter game name: ").strip()
            if not gameName:
                print("Game name cannot be empty!")
                continue
            games.append(Game(gameName))
            print(f"\n✅ Game '{gameName}' created!")
        case 3:
            if not games:
                print("No games available! Create a game first.")
                continue
            printHeader("SELECT GAME")
            for idx, game in enumerate(games, 1):
                print(f"[{idx}] {game.name}")
            try:
                gameChoice = int(input("Select game: "))
                currentGame = games[gameChoice-1]
            except (ValueError, IndexError):
                print("Invalid game selection!")
                continue
            printHeader("GAME MODES")
            mode = input(
                "[1] Play Against Bots (Player Vs Agent Vs ...)\n"
                "[2] Auto Battle (Agents Vs Agents Vs ...)\n"
                "[3] (Player Vs Player Vs ...)\n"
                "Input => "
            )
            if mode == '1':
                if len(agents) < 2:
                    print("Need at least 2 agents to play!")
                    continue
                player = selectAgent("Select your agent: ")
                bots = [a for a in agents if a.isBot and a != player]
                if not bots:
                    print("No Bots Available, Create Bot Agents First")
                    continue
                currentGame.displayBoard()
                currentGame.startGameWithBot([player] + bots[:3])
            elif mode == '2':
                if len(agents) < 2:
                    print("Need At Least 2 Agents For Auto Play")
                    continue
                currentGame.autoPlay(agents)
                currentGame.displayBoard()
            elif mode == '3':
                if len(agents) < 1:
                    print("Need At Least 1 Agent To Play")
                    continue
                printHeader("MANUAL MULTIPLAYER")
                currentGame.displayBoard()
                turn = 0
                while currentGame.isBoardAvailable:
                    current_agent = agents[turn % len(agents)]
                    try:
                        col = int(input(
                            f"\n{current_agent.username}'s turn ({current_agent.color})\n"
                            "Enter column (1-7): "
                        ))
                        if 1 <= col <= 7:
                            if currentGame.makeMove(current_agent, col):
                                currentGame.displayBoard()
                                turn += 1
                            else:
                                print("Column full! Try another.")
                        else:
                            print("Invalid column! (1-7 only)")
                    except ValueError:
                        print("Numbers only!")
            else:
                print("Invalid Game Mode Selection!")
        case 4:
            print("Thanks For Playing!")
            break
        case _:
            print("Invalid Option! Please Choose 1-4.")