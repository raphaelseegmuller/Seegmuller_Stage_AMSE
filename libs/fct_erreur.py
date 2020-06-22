def erreur(y_obs, y_pred):
    assert len(y_obs) == len(y_pred)
    res = 0
    for t_value in range(len(y_obs)):
        res += (y_obs[t_value] - y_pred[t_value]) ** 2
    return res