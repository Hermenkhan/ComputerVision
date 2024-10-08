# -*- coding: utf-8 -*-
"""EDA using bivariate-analysis.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1JO4KHpDZZFsasYDtPghyBgkgZnd3lPTn

# EDA using bivariate-analysis
"""

import pandas as pd
import seaborn as sns

tips = sns.load_dataset('tips')

tips.head()

titanic = pd.read_csv('train.csv')

flights = sns.load_dataset('flights')

flights.head()

iris = sns.load_dataset('iris')

iris

"""## 1. Scatterplot (Numerical - Numerical)"""

# sns.scatterplot(tips['total_bill'],tips['tip'])
sns.scatterplot(data=tips, x='total_bill', y='tip')

#sns.scatterplot(tips['total_bill'],tips['tip'],hue=tips['sex'])
sns.scatterplot(data=tips, x='total_bill', y='tip', hue='sex')

#sns.scatterplot(tips['total_bill'],tips['tip'],hue=tips['sex'],style=tips['smoker'])
sns.scatterplot(data=tips, x='total_bill', y='tip', hue='sex', style='smoker')

#sns.scatterplot(tips['total_bill'],tips['tip'],hue=tips['sex'],style=tips['smoker'],size=tips['size'])
sns.scatterplot(data=tips, x='total_bill', y='tip', hue='sex', style='smoker', size='size')

"""## 2. Bar Plot (Numerical - Categorical)"""

titanic.head()

#sns.barplot(titanic['Pclass'],titanic['Age'],hue=titanic['Sex'])
sns.barplot(data=titanic, x='Pclass', y='Age', hue='Sex')

#sns.barplot(titanic['Pclass'],titanic['Age'])
sns.barplot(data=titanic, x='Pclass', y='Age')

"""## 3. Box Plot (Numerical - Categorical)"""

#sns.boxplot(titanic['Sex'],titanic['Age'],hue=titanic['Survived'])
sns.boxplot(data=titanic, x='Sex', y='Age', hue='Survived')

"""## 4. Distplot (Numerical - Categorical)"""

sns.distplot(titanic[titanic['Survived']==0]['Age'])

sns.distplot(titanic[titanic['Survived']==1]['Age'],hist=False)

"""## 5. HeatMap (Categorical - Categorical)"""

titanic.head(3)

pd.crosstab(titanic['Pclass'],titanic['Survived'])

sns.heatmap(pd.crosstab(titanic['Pclass'],titanic['Survived']))

#(titanic.groupby('Embarked').mean()['Survived'])
titanic.groupby('Embarked')['Survived'].mean()

#(titanic.groupby('Embarked').mean()['Survived']*100)
titanic.groupby('Embarked')['Survived'].mean()*100

"""## 6. ClusterMap (Categorical - Categorical)"""

pd.crosstab(titanic['Parch'],titanic['Survived'])

"""# Dendrogram
Tree diagram used to illustrate the arrangement of the clusters produced by hierarchical clustering

A dendrogram is a diagram representing a tree. This diagrammatic representation is frequently used in different contexts

Hierarchical clustering is where you build a cluster tree (a dendrogram) to represent data, where each group (or “node”) links to two or more successor groups. The groups are nested and organized as a tree, which ideally ends up as a meaningful classification scheme.
"""

sns.clustermap(pd.crosstab(titanic['Parch'],titanic['Survived']))

"""## 7. Pairplot"""

iris.head()

sns.pairplot(iris)

sns.pairplot(iris,hue='species')

flights.head()

flights.shape

flights

flights.pivot_table(values='passengers',index='month',columns='year')

sns.heatmap(flights.pivot_table(values='passengers',index='month',columns='year'))

sns.clustermap(flights.pivot_table(values='passengers',index='month',columns='year'))

