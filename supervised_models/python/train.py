"""
Trains the ONS fastText model by generating text corpa from ONS publications
@author David Sullivan 01/06/18
"""


def train_model(fname_prefix: str, out_fname: str, label_prefix: str="__label__", **kwargs):
    # Train the model
    import fastText

    params = {
        "dim": kwargs.get("dim", 300),
        "epoch": kwargs.get("epoch", 1000),
        "wordNgrams": kwargs.get("wordNgrams", 2),
        "verbose": kwargs.get("verbose", 2),
        "minCount": kwargs.get("minCount", 15),
        "minCountLabel": kwargs.get("minCountLabel", 5),
        "lr": kwargs.get("lr", 0.1),
        "neg": kwargs.get("neg", 10),
        "thread": kwargs.get("thread", 16),
        "loss": kwargs.get("loss", "ns"),
        "t": kwargs.get("t", 1e-5)
    }

    print("Training fastText model...")
    print("Params:", params)
    model = fastText.train_supervised(input="%s.train" % fname_prefix, label=label_prefix, **params)
    print("Saving...")
    model.save_model(out_fname)
    print("Done")
    return model
