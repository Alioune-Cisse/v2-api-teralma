import pandas as pd
class Datasets:
    def __init__(self, ceremonie="Mariage"):
        self.ceremonie = ceremonie

    def read_data(self):
        if (self.ceremonie == "Mariage"):
            files = "Data/data_alain.xlsx"
            data = pd.read_excel(
                files, header=[2], usecols=[i for i in range(6)]
            )
            # Rename column
            data.rename(
                    columns={"Unnamed: 1": "Sous catégories dépenses"},
                        inplace=True)
            # Remplacer les nan par la valeur du dessus
            data['Catégories dépenses'] = pd.Series(
                    data['Catégories dépenses']
            ).fillna(method='ffill')

        elif (self.ceremonie == "Baptême"):
            pass

        else:
            pass
        
        super_marche = pd.read_csv("Data/super_marche.csv")
        produits_beautes = pd.read_csv("Data/produits beaute.csv", 
                                       encoding= 'unicode_escape')
        
        
        # Convertir en lower
        data = data.apply(lambda x: x.astype(str).str.lower())

        return data, super_marche, produits_beautes
    
    
    
    
    def all_values(self):
        data, super_marche, produits_beautes = self.read_data()
        val1 = data['Sous catégories dépenses'].tolist()
        val2 = super_marche["Produit"].tolist()
        val3 = produits_beautes["Product"].tolist()
        return [*val1, *val2, *val3]