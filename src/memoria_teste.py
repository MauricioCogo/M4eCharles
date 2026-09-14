from src.memory_detector import MemoryDetector


detector = MemoryDetector()

message = input("Mensagem: ")

memory = detector.detect(message)

print("Memória detectada:", memory)