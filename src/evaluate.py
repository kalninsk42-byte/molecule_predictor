from sklearn.metrics import mean_squared_error, r2_score

def evaluate(model, X_test, y_test):
    preds = model.predict(X_test)

    rmse = mean_squared_error(y_test, preds) ** 0.5
    r2 = r2_score(y_test, preds)

    print("\n📊 Model Evaluation")
    print("-------------------")
    print("RMSE:", rmse)
    print("R2 Score:", r2)