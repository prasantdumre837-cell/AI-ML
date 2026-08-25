df_clean['Join_Year'] = df_clean['Join_Date'].dt.year
yearly_joins = df_clean.groupby('Join_Year').size()

plt.figure(figsize=(8, 4))
plt.plot(yearly_joins.index, yearly_joins.values, marker='o', color='darkorange', linewidth=2)
plt.title('New Hires Count by Year')
plt.xlabel('Year')
plt.ylabel('Number of Hires')
plt.xticks(yearly_joins.index)
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()