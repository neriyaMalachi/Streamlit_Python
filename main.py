import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


movies_data = pd.read_csv('./movies.csv')
# כותרת לגרף
st.write("Average Move Budget, Grouped by Genre")
# חישוב ממוצע על פי זאנר
avg_budget = movies_data.groupby('genre')['budget'].mean().round()
# מאפס לו את index ומסדר אותם מחדש
avg_budget = avg_budget.reset_index()

# מקבל את הערכים שהוא רוצה
genre = avg_budget['genre']
avg_bud = avg_budget['budget']

#יוצר כנבס בגודל מסוים בכדי ליצור עליו את הגרף
fig = plt.figure(figsize=(19,10))

# מיצר את הגרף כולל צבע וערכים
plt.bar(genre,avg_bud,color='maroon')

# נותן שמות לlable
plt.xlabel('genre')
plt.ylabel('budget')
plt.title('Matplotlib Bar Chart Showing the Average \
Budget of Movies in Each Genre')



#מריץ את השרת עם הגרף שיצרנו
st.pyplot(fig)

# col1, col2 =st.columns(2)
# col1.write('hello col1')
# col2.write('hello col2')
#
# plt.show()


score_rating = movies_data['score'].unique().tolist()
genre_rating = movies_data['genre'].unique().tolist()
year_rating = movies_data['year'].unique().tolist()










