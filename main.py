from led_controller import LEDController
import time

def main():
    led_pin = 27  # Usa el pin GPIO 27
    led = LEDController(led_pin)
    
    try:
        print("Iniciando el efecto neón estropeado...")
        led.blink_neon_effect(10)  # Ejecuta el efecto por 10 segundos
    finally:
        led.cleanup()
        print("Limpieza y apagado.")

if __name__ == "__main__":
    main()