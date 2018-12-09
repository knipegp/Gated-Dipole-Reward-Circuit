import normal_gated_dipole
import modulated_circuit


def main():
    # normal_circuit = normal_gated_dipole.NormalGatedDipole(a_rate=5,
    #                                                        b_max_level=1,
    #                                                        time_step=.001,
    #                                                        steps=1000,
    #                                                        tonic_max=1,
    #                                                        tonic_min=0,
    #                                                        phasic_duty_cycle=.5,
    #                                                        phasic_max=10,
    #                                                        phasic_min=0)
    # normal_circuit.execute()
    # normal_circuit.plot()

    modulated_circ = modulated_circuit.ModulatedCircuit(a_rate=5,
                                                        b_max_level=1,
                                                        b_reduction_rate=.025,
                                                        time_step=.001,
                                                        steps=1000,
                                                        tonic_max=1,
                                                        tonic_min=0,
                                                        phasic_duty_cycle=.5,
                                                        phasic_max=10,
                                                        phasic_min=.5)

    modulated_circ.execute(runs=20)

    modulated_circ.plot(run_index=1)
    modulated_circ.plot(run_index=10)
    modulated_circ.plot(run_index=20)


if __name__ == '__main__':
    main()

