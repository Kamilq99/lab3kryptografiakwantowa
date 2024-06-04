import qiskit

# Inicjalizacja qubitów
q = qiskit.QuantumCircuit(6)

# Stosowanie bramek Hadamarda na qubity 0, 3, 4 i 5
q.h(0)
q.h(3)
q.h(4)
q.h(5)

# Stosowanie bramek CNOT na qubity 0 i 1, 1 i 2, 2 i 3, 3 i 4, 4 i 5
q.cx(0, 1)
q.cx(1, 2)
q.cx(2, 3)
q.cx(3, 4)
q.cx(4, 5)

# Stosowanie bramki X na qubit 2
q.x(2)

# Pomiar qubitów 0-5
q.measure_all()

# Uruchamianie symulatora
backend = qiskit.Aer.get_backend('qvm')
job = qiskit.execute(q, backend, shots=1024)
result = job.result().get_counts()

# Wyświetlanie wyników
print(result)