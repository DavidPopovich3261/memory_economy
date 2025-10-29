import io1,game




def play():
    z = io1.input_size()
    l = game.creating_a_card_deck(z)
    s = game.parallel_matrix(z)
    n=game.Creat_plger()
    flag=True
    while flag:
        flag=game.Steps(n)
        game.step_move(l, s,n)
        flag=game.is_won(n,z)
        if not flag:
            io1.print_metrix(l)


play()
