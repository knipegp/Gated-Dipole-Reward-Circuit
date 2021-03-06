from matplotlib import pyplot as plt

from circuits import normal_gated_dipole, modulated_circuit


def main():
    normal_circuit = normal_gated_dipole.NormalGatedDipole(a_rate=5,
                                                           b_max_level=1,
                                                           time_step=.001,
                                                           steps=1000,
                                                           tonic_max=1,
                                                           tonic_min=0,
                                                           phasic_duty_cycle=.5,
                                                           phasic_max=10,
                                                           phasic_min=0)
    normal_circuit.execute(runs=1)
    normal_circuit.plot(run_index=1)

    modulated_circ = modulated_circuit.ModulatedCircuit(a_rate=5,
                                                        b_max_level=1,
                                                        b_reduction_rate=.03,
                                                        time_step=.001,
                                                        steps=1000,
                                                        tonic_max=1,
                                                        tonic_min=0,
                                                        phasic_duty_cycle=.5,
                                                        phasic_max=10,
                                                        phasic_min=.5,
                                                        min_reduction=1/5)

    while modulated_circ.phasic_input.phasic_probability < .99:
        modulated_circ.execute(runs=1)

    modulated_circ.plot(run_index=[1,
                                   int(len(modulated_circ.phasic_input.output)/2),
                                   len(modulated_circ.phasic_input.output)-1])

    modulated_circ.plot_uses()

    list_of_runs = list()
    for idx in range(1000):
        runs_to_addiction = 0
        addiction_average = modulated_circuit.ModulatedCircuit(a_rate=5,
                                                               b_max_level=1,
                                                               b_reduction_rate=.03,
                                                               time_step=.001,
                                                               steps=1000,
                                                               tonic_max=1,
                                                               tonic_min=0,
                                                               phasic_duty_cycle=.5,
                                                               phasic_max=10,
                                                               phasic_min=.5,
                                                               min_reduction=1 / 5)

        while addiction_average.phasic_input.phasic_probability < .99:
            addiction_average.execute(runs=1)
            runs_to_addiction = runs_to_addiction + 1

        list_of_runs.append(runs_to_addiction)

        # Used to check progress. Make sure machine isn't frozen.
        if idx % 50 == 0:
            print(idx)

    plt.Figure()
    plt.hist(list_of_runs, bins=10)
    plt.title('Number of Runs to Addiction Histogram')
    plt.ylabel('Iterations of Model')
    plt.xlabel('Number of Runs to Addiction')
    plt.show()


if __name__ == '__main__':
    main()

