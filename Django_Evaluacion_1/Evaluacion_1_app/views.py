from django.shortcuts import render

# Create your views here
def index(request):

    return render(request, 'Evaluacion_1_app/index.html')  

def ProdCPersonal(request):
    data = {
        "titulo":"Cuidado Personal",
        "categoria": "personal",
        "producto1": "Multigroom serie 2400 King",
        "producto2": "Sonicare protective clean King",
        "producto3": "Secador de pelo term serie 5000 King",
        "foto1": "cpersonal1.jpg",
        "foto2": "cpersonal2.jpg",
        "foto3": "cpersonal3.jpg",
        }
    return render(request, 'Evaluacion_1_app/productos.html', data)
    

def ProdDermo(request):
    data = {
        "titulo":"Dermo-cosmética",
        "categoria" : "dermo",
        "producto1": "Super serum facial King 30 ml",
        "producto2": "Protector solar spray factor-50 Sun 200 ml ",
        "producto3": "Gel limpiador anti-impurezas King 250 ml",
        "foto1": "dermo1.jpg",
        "foto2": "dermo2.jpg",
        "foto3": "dermo3.jpg",
        }
    return render(request, 'Evaluacion_1_app/productos.html', data)

def ProdSupl(request):
    data = {
        "titulo":"Suplementos",
        "categoria": "sup",
        "producto1": "Proteínas 1kg Vitalix",
        "producto2": "Aminoácidos 30 sobres Vitalix",
        "producto3": "Biotín vegetal 30 cápsulas Vitalix",
        "foto1": "sup1.jpg",
        "foto2": "sup2.jpg",
        "foto3": "sup3.jpg",
        }
    return render(request, 'Evaluacion_1_app/productos.html', data)


def Usuario(request):
    data = {
        "titulo1":"Información del usuario",
        "titulo2":"Ficha personal",
        "foto":"perfil.jpg",
        "id": "1", 
        "nombre": "Alyson Diaz", 
        "rut": "15.798.0093-9",         
        "fechaNac": "05/09/1989", 
        "direccion": "Leon Gallo # 0700", 
        "email": "alyson.diaz@gmail.com",
        "comuna": "Temuco", 
        "telefono": "+569-92873914"
            }
    return render(request, 'Evaluacion_1_app/registro.html', data)

def Descripcion(request, categoria, producto):   
    categoria = {
        "personal":{ "producto1":"Recortador para nariz: elimina suavemente el vello no deseado de la nariz y los oídos. Recortador sin peine: Empléalo para conseguir líneas limpias y definidas en los bordes de tu barba, cuello y nacimiento del cabello. Batería. Obtén hasta 60 minutos de uso inalámbrico por cada carga de 16 horas.",
                     "producto2":"La tecnología sónica combinada con nuestra acción de cepillado elimina suavemente hasta 3 veces más placa* que un cepillo dental manual Este cepillo posee 1 modo de cepillado, 1 intensidad, 1 cabezal, 1 cargador usb y 1 estuche de viaje.",
                     "producto3":"Secador de pelo de formato pequeño equipado con un dispositivo electromecánico que expulsa aire caliente o frío sobre el pelo húmedo o mojado. De esta forma acelera la evaporación del agua para secar el cabello. Suele ser un aparato muy común en todas las casas e incluso en hoteles.",
                    },

        "dermo":    {"producto1":"Sérum o suero cosmético es un tratamiento que se caracteriza por tener una alta concentración de ingredientes activos y una textura líquida que favorecen una rápida y más profunda absorción. Su principal beneficio es su alta eficacia para combatir el envejecimiento prematuro de la piel",
                     "producto2":"Su fórmula de protección solar ultraligera contiene filtros Foto-Estables Avanzados UVA y UVB, Vitaminas y Extractos de Diferentes Hierbas que ayudan a proteger la piel contra el daño solar, cómo las manchas o diferente pigmentación y la formación de arrugas prematuras.",
                     "producto3":"Limpia los poros de la piel dejando que respiren y queden libre de grasas, contaminación y células muertas. Además desinflama y rejuvenece tu piel gracias a sus ingredientes activos, el aloe vera, caléndula y centella asiática.",  
                    },

        "sup":      {"producto1":"suplemento alimenticio a base de proteína de suero de leche (whey) diseñada especialmente para cocinar. Es un suplemento deportivo y alimenticio de alta calidad nutricional, rico en proteínas, aminoácidos ramificados y bajo en carbohidratos y grasas.",
                     "producto2":"moléculas que se combinan para formar proteínas. Los aminoácidos y las proteínas son los pilares fundamentales de la vida. Cuando las proteínas se digieren o se descomponen, el resultado son los aminoácidos.",
                     "producto3":"La biotina es una vitamina B que se encuentra en muchos alimentos y ayuda a convertir los carbohidratos, las grasas y las proteínas que consume en energía que usted necesita. ",  
                    }
           
        }
    """productos ={ 
        "personal":{"producto1": "Multigroom serie 2400 King",
                    "producto2": "Sonicare protective clean King",
                    "producto3": "Secador de pelo term serie 5000 King",
                    },

        "dermo":    {"producto1": "Super serum facial King 30 ml",
                     "producto2": "Protector solar spray factor-50 Sun 200 ml ",
                     "producto3": "Gel limpiador anti-impurezas King 250 ml",
                    },

        "sup":      {"producto1": "Proteínas 1kg Vitalix",
                     "producto2": "Aminoácidos 30 sobres Vitalix",
                     "producto3": "Biotín vegetal 30 cápsulas Vitalix"
                    }
        }"""
    Descr= categoria.get(categoria, {}).get(producto, "No disponible")
  
    



    data = {
        "titulo":"Descripcion",
        "producto":producto,
        "descripcion": Descr,

       
    }

    return render(request, 'Evaluacion_1_app/descripcion.html',data)

