from src.charles import Charles
import textwrap

def clean_text(text):
    text = text.replace("**", "")
    text = text.replace("__", "")
    return text

def format_text(text, width=100):
    paragraphs = text.split("\n\n")
    
    formatted_paragraphs = []
    
    for paragraph in paragraphs:
        lines = paragraph.split("\n")
        formatted_lines = []
        
        for line in lines:
            if not line.strip():
                formatted_lines.append("")
                continue
            
            formatted_line = textwrap.fill(line, width=width, replace_whitespace=False, drop_whitespace=False)
            
            formatted_lines.append(formatted_line)
            
        formatted_paragraphs.append("\n".join(formatted_lines))

    return "\n\n".join(formatted_paragraphs)


def main():
    charles = Charles()

    print("Charles iniciado.")
    print("Digite 'sair' para encerrar.\n")
    print("Use /memoria <texto> para adicionar uma memória.\n")

    while True:
        prompt = input("Você: ")

        if prompt.lower() == "sair":
            break
        
        if prompt.lower().startswith("/memoria"):
            memory_content = prompt.replace("/memoria","", 1)
            
            charles.memory.add(memory_content.strip())
            
            print("\nMemória adicionada com sucesso!\n")
            
            continue
        
        response = charles.ask(prompt)
        memory = response[1]  # Get the memory candidate from the response tuple
        
        formatted = format_text(response[0] , width=100)
        formatted = clean_text(formatted)
        print(f"\n{formatted}\n")
        
        if memory:
            print(f"\nMemória detectada: {memory}\n")
            
            choice = input("Deseja adicionar esta memória? (s/n): ")
            
            if(choice.lower() == "s"):
                charles.memory.add(memory)
                print("\nMemória adicionada com sucesso!\n")
        
        
        

if __name__ == "__main__":
    main()
    
