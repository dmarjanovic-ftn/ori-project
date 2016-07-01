from keras.callbacks import ModelCheckpoint
from keras.models import Sequential
from keras.layers import Dense, Dropout
import numpy


# TODO or FIXME - Delete or change
def train_first():
    # fix random seed for reproducibility
    seed = 7
    numpy.random.seed(seed)
    # load pima indians dataset
    dataset = numpy.loadtxt("output-3.csv", delimiter=",")
    # split into input (X) and output (Y) variables
    X = dataset[:,0:32]
    Y = dataset[:,32:]

    print X[0]
    print len(X[0])
    print Y
    print len(Y)

    # create model
    model = Sequential()
    model.add(Dense(16, input_dim=32, init='uniform', activation='linear'))
    model.add(Dense(8, init='uniform', activation='linear'))
    model.add(Dense(1, init='uniform', activation='linear'))
    # Compile model
    model.compile(loss='mean_squared_error', optimizer='sgd', metrics=['accuracy'])
    # Fit the model
    model.fit(X, Y, nb_epoch=10, validation_split=0.2, batch_size=32)
    # evaluate the model
    scores = model.evaluate(X, Y)
    print("%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))


def create_model():
    # Kreiranje modela
    model = Sequential()
    model.add(Dense(10, input_dim=24, input_shape=(1, 24), init='uniform', activation='linear'))
    # model.add(Dense(12, init='uniform', activation='linear'))
    model.add(Dense(8, init='uniform', activation='linear'))
    return model

def train_tree_figures_input_one_figure_output():
    # Ucitavamo skup generisanih primjera
    dataset = numpy.loadtxt("../docs/generated-examples.csv", delimiter=",")

    # Dobijamo ulazne podatke (input_data) i izlazne podatke (output_data)
    input_data  = dataset[:, 0:24]
    output_data = dataset[:, 24:]

    # input_data  = input_data / input_data.max(axis=0)
    # output_data = output_data / output_data.max(axis=0)
    model = create_model()

    # Kompajliranje modela
    model.compile(loss='mean_squared_error', optimizer='sgd', metrics=['accuracy'])

    # Fitovanje modela
    checkpointer = ModelCheckpoint(filepath="../docs/weights.hdf5", verbose=1, save_best_only=True)
    model.fit(input_data, output_data, nb_epoch=50, validation_split=0.2, batch_size=32, callbacks=[checkpointer])

    # Evauliranje modela
    scores = model.evaluate(input_data, output_data)

    # Cuvanje modela i velicina u datoteku
    # json_string = model.to_json()
    # open('../docs/model.json', 'w').write(json_string)
    # open('../docs/weights.txt', 'w').write(str(model.get_weights()))


    # Ucitavanje modela i postavljanje tezina (FIXME)
    # model = model_from_json(open('model.json').read())
    # model.set_weights(weights)

    print("%s: %.2f%%" % (model.metrics_names[1], scores[1] * 100))

    dataset = numpy.loadtxt("../docs/generated-test-examples.csv", delimiter=",")
    test_in = dataset[:, 0:24]
    test_out = dataset[:, 24:]

    for i in xrange(20):
        _input = numpy.array(test_in[i])[None]
        print "\n" + 80 * "-"
        print model.predict_on_batch(_input)
        print test_out[i]


def load_trained_model():
    model = create_model()
    model.load_weights("../docs/weights.hdf5")
    return model

if __name__ == "__main__":
    #load_trained_model()

    train_tree_figures_input_one_figure_output()
