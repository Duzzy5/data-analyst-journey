importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": rf_model.feature_importances_
})

importance = importance.sort_values(
    by="Importance",
    ascending=False
)

print(importance)

#Graph for the same thing
importance.plot(
    x="Feature",
    y="Importance",
    kind="bar",
    figsize=(8,4)
)
