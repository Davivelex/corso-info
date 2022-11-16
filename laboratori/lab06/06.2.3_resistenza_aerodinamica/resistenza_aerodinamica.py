def force(v):
    return (1/2) * 1.23 * (v ** 2) * 2.5 * 0.2


velocity = float(input("Inserisci velocità auto: "))

power = force(velocity) * velocity
print(f"La macchina deve sviluppare almeno {power:.2f}W")
power /= 735.5
print(f"La macchina deve sviluppare almeno {power:.2f}CV")
