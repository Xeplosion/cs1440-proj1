import engine
import ai
import interface

if __name__ == '__main__':
    while True:
        interface.logo()
        mode = interface.player_select()
        if mode == 0:
            engine.cpu_vs_cpu(ai.strategy_optimal, ai.strategy_optimal)
        elif mode == 1:
            engine.human_vs_cpu(ai.strategy_optimal)
        elif mode == 2:
            engine.cpu_vs_human(ai.strategy_optimal)
        elif mode == 3:
            engine.human_vs_human()
        elif mode == 4:
            engine.game(ai.strategy_optimal, ai.strategy_optimal)
        else:
            break
    print("Thanks for playing!")
