from pydfs_lineup_optimizer import Site, Sport, get_optimizer


optimizer = get_optimizer(Site.DRAFTKINGS, Sport.BASEBALL)
optimizer.load_players_from_csv("DKSalaries.csv")
lineup_generator = optimizer.optimize(10)
for lineup in lineup_generator:
    print(lineup)
optimizer.print_statistic()
