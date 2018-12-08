import normal_gated_dipole


def main():
    normal_circuit = normal_gated_dipole.NormalGatedDipole()
    normal_circuit.execute()
    normal_circuit.plot()


if __name__ == '__main__':
    main()

