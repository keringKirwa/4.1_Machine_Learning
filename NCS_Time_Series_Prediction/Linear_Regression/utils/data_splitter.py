def __dynamic_data_split(X, y, ratio_train):
    """
    Splits data and labels into training, validation, and test sets.

    Args:
        X (a 2D numpy.ndarray): Data.
        y (numpy.ndarray): Labels.
        ratio_train (float): Ratio for training data.

    Returns:
        tuple: (X_train, y_train, X_val, y_val, X_test, y_test).
    """
    total_samples = X.shape[0]

    train_samples = int(ratio_train * total_samples)

    X_train, y_train = X[:train_samples], y[:train_samples]
    X_test, y_test = X[train_samples:], y[train_samples:]

    return X_train, y_train, X_test, y_test
