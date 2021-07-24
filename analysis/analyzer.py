import pandas as pd


class Analyzer:
	def __init__(self):
		self.__df = None
		self.__df_path = "./data/covid-data.csv"
		self.__result_dict = {}
		self.__confirmados = []	
		self.__obitos = []
		self.__tx_obitos = []
		self.__recuperados = []
		self.__tx_recuperados = []
		self.__isolamento = []
		self.__tx_isolamento = []
		self.__enfermaria = []
		self.__leitos_enf = []
		self.__tx_oc_enf = []
		self.__tx_enfermaria = []
		self.__uti = []
		self.__leitos_uti = []
		self.__tx_uti = []
		self.__tx_oc_uti = []
		self.__testes_novos = []
		self.__testes_acumulados = []
		self.__tx_testes = []

		self._create_df()
		self._treatment()
		self._analyze()

	def _create_df(self):
		self.__df = pd.read_csv(self.__df_path)
		self.__df = self.__df[self.__df["dt_referencia"].notnull()]

	def _treatment(self):
		self.__df["confirmados"].fillna(0, inplace = True)
		self.__df["obitos"].fillna(0, inplace = True)
		self.__df["tx_obitos"].fillna(0, inplace = True)
		self.__df["recuperados"].fillna(0, inplace = True)
		self.__df["tx_recuperados"].fillna(0, inplace = True)
		self.__df["isolamento"].fillna(0, inplace = True)
		self.__df["tx_isolamento"].fillna(0, inplace = True)
		self.__df["enfermaria"].fillna(0, inplace = True)
		self.__df["tx_enfermaria"].fillna(0, inplace = True)
		self.__df["uti"].fillna(0, inplace = True)
		self.__df["tx_uti"].fillna(0, inplace = True)
		self.__df["testes_novos"].fillna(0, inplace = True)
		self.__df["testes_acumulados"].fillna(0, inplace = True)
		self.__df["tx_testes"].fillna(0, inplace = True)
		self.__df["leitos_uti"].fillna(0, inplace = True)
		self.__df["tx_oc_uti"].fillna(0, inplace = True)
		self.__df["leitos_enf"].fillna(0, inplace = True)
		self.__df["tc_oc_enf"].fillna(0, inplace = True)
		

	def _analyze(self):

		self.__confirmados = self.__df["confirmados"].tolist()
		self.__obitos = self.__df["obitos"].tolist()
		self.__tx_obitos = self.__df["tx_obitos"].tolist()
		self.__recuperados = self.__df["recuperados"].tolist()
		self.__tx_recuperados = self.__df["tx_recuperados"].tolist()
		self.__isolamento = self.__df["isolamento"].tolist()
		self.__tx_isolamento = self.__df["tx_isolamento"].tolist()
		self.__enfermaria = self.__df["enfermaria"].tolist()
		self.__leitos_enf = self.__df["leitos_enf"].tolist()
		self.__tx_oc_enf = self.__df["tc_oc_enf"].tolist()
		self.__tx_enfermaria = self.__df["tx_enfermaria"].tolist()
		self.__uti = self.__df["uti"].tolist()
		self.__leitos_uti = self.__df["leitos_uti"].tolist()
		self.__tx_uti = self.__df["tx_uti"].tolist()
		self.__tx_oc_uti = self.__df["tx_oc_uti"].tolist()
		self.__testes_novos = self.__df["testes_novos"].tolist()
		self.__testes_acumulados = self.__df["testes_acumulados"].tolist()
		self.__tx_testes = self.__df["tx_testes"].tolist()

	@property
	def confirmados(self):
		response = dict()
		response["confirmados"] = self.__confirmados
		
		return response

	@property
	def obitos(self):
		response = dict()
		response["obitos"] = self.__obitos
		
		return response

	@property
	def tx_obitos(self):		
		response = dict()
		response["tx_obitos"] = self.__tx_obitos

		return response

	@property
	def recuperados(self):
		response = dict()
		response["recuperados"] = self.__recuperados

		return response

	@property
	def tx_recuperados(self):
		response = dict()
		response["tx_recuperados"] = self.__tx_recuperados

		return response

	@property
	def isolamento(self):
		response = dict()
		response["isolamento"] = self.__isolamento

		return response

	@property
	def tx_isolamento(self):
		response = dict()
		response["tx_isolamento"] = self.__tx_isolamento

		return response

	@property
	def enfermaria(self):
		response = dict()
		response["enfermaria"] = self.__enfermaria

		return response

	@property
	def leitos_enf(self):
		response = dict()
		response["leitos_enf"] = self.__leitos_enf

		return response

	@property
	def tx_oc_enf(self):
		response = dict()
		response["tx_oc_enf"] = self.__tx_oc_enf

		return response

	@property
	def tx_enfermaria(self):
		response = dict()
		response["tx_enfermaria"] = self.__tx_enfermaria

		return response

	@property
	def uti(self):
		response = dict()
		response["uti"] = self.__uti

		return response

	@property
	def leitos_uti(self):
		response = dict()
		response["leitos_uti"] = self.__leitos_uti

		return response

	@property
	def tx_uti(self):
		response = dict()
		response["tx_uti"] = self.__tx_uti

		return response

	@property
	def tx_oc_uti(self):
		response = dict()
		response["tx_oc_uti"] = self.__tx_oc_uti

		return response

	@property
	def testes_novos(self):
		response = dict()
		response["testes_novos"] = self.__testes_novos

		return response
	
	@property
	def testes_acumulados(self):
		response = dict()
		response["testes_acumulados"] = self.__testes_acumulados

		return response

	@property
	def tx_testes(self):
		response = dict()
		response["tx_testes"] = self.__tx_testes

		return response















