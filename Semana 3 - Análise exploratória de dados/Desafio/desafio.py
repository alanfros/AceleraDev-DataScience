import pandas as pd
df = pd.read_csv('desafio1.csv')

santa_catarina = df.loc[df['estado_residencia'] == 'SC']['pontuacao_credito']
rio_gran_sul = df.loc[df['estado_residencia'] == 'RS']['pontuacao_credito']
parana = df.loc[df['estado_residencia'] == 'PR']['pontuacao_credito']

submission = {
    "SC": {
        "moda": santa_catarina.mode()[0],
        "mediana": santa_catarina.median(),
        "media": santa_catarina.mean(),
        "desvio_padrao": santa_catarina.std()},
    "RS": {
        "moda": rio_gran_sul.mode()[0],
        "mediana": rio_gran_sul.median(),
        "media": rio_gran_sul.mean(),
        "desvio_padrao": rio_gran_sul.std()},
    "PR": {
        "moda": parana.mode()[0],
        "mediana": parana.median(),
        "media": parana.mean(),
        "desvio_padrao": parana.std()}
}

submission = str(submission)
submission = submission.replace("\'", "\"")
open('submission.json', 'w').write(submission)
