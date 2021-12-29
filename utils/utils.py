import matplotlib.pyplot as plt

def month_converter(date:str) -> str:
    '''Converts month in portuguese language to the respective number.'''
    months = {
        'janeiro':1,
        'fevereiro':2, 
        'março':3,
        'abril':4,
        'maio':5,
        'junho':6,
        'julho':7,
        'agosto':8,
        'setembro':9,
        'outubro':10,
        'novembro':11,
        'dezembro':12
    }
    return months[date.lower()]

def money_treatment(money:str) -> float:
    '''Formats money in reais to a float.'''
    return float(money.replace("R$",'').replace('.','')
                 .replace(',','.').replace('\n',''))

def plot_configuration(x_label:str, y_label:str, title: str = '',) -> None:
    '''Sets plot configurations.'''                   
    ax = plt.subplot(111)
    ax.set_title(title, fontsize=20)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    #plt.xscale('log')
    plt.xlabel(x_label,fontsize=16)
    plt.ylabel(y_label,fontsize=16)
    plt.subplots_adjust(top=0.88, bottom=0.20, left=0.18, right=0.78, 
                        hspace=0.56, wspace=0.20)
    plt.figtext(0.35, 0.025,"Autor: Vitor Junior",
                fontsize=10)  
    return None
