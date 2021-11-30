# %%
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = (8, 4)
plt.rcParams['figure.dpi'] = 150
plt.rc('legend', fontsize=9)

# %%
df = pd.read_csv("naruto.csv")

# %%
(1/500)*(df  .
         groupby("Type").size())


# %%
sns.barplot(data=gtype, x='Type', y="size", palette="Set2")


# %%
sns.lineplot(data=df, x="Num_episode", y="Rate", color="black")
plt.xlabel("Number of Episode")
plt.title("Rate over time")
# %%
df[df.Rate == df['Rate'].max()]

df[df.Rate == df['Rate'].min()]
# %%
df[["Season", "Name of Season"]] = df["Saga"].str.split(' ', 1, expand=True)
# %%
seasons = df .\
    groupby("Season", as_index=False)[["Rate", "Votes"]] .\
    mean() .\
    sort_values("Rate", ascending=False)
# %%

sns.catplot(data=df, x="Rate", y="Season", hue="Type")
# %%
sns.plot(data=seasons, x="Rate", y="Season", kind="bar")
plt.xlabel("Mean Rate")
# %%
seasons
