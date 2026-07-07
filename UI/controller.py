import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model


    def handleCreaGrafo(self, e):
        self._model.buildGraph()
        nNodi, nArchi = self._model.getGraphDetails()

        self._view._txt_result.controls.clear()
        self._view._txt_result.controls.append(
            ft.Text("Grafo correttamente creato.")
        )
        self._view._txt_result.controls.append(
            ft.Text(f"Numero nodi: {nNodi}")
        )
        self._view._txt_result.controls.append(
            ft.Text(f"Numero di archi: {nArchi}")
        )

        self._view.update_page()

    def handleStampaInfo(self,e):
        self._view._txt_result.controls.clear()

        numero, largest, dettagli = self._model.getConnessaInfo()
        self._view._txt_result.controls.append(
            ft.Text(f"Numero di componenti connesse: {numero}")
        )
        self._view._txt_result.controls.append(
            ft.Text(f"Dimensione della componente connessa più grande: {len(largest)} album")
        )
        self._view._txt_result.controls.append(
            ft.Text("Dettagli degli album appartenenti alla componente connessa più grande:")
        )
        for titolo, num_brani in dettagli:
            self._view._txt_result.controls.append(ft.Text(f"{titolo}: {num_brani} brani"))
        self._view.update_page()

    def fillDDsAlbum(self):
        albums = self._model.getAllNodes()

        albumsOptions = list(map(lambda x: ft.dropdown.Option(x), albums))
        self._view._ddAlbum.options = albumsOptions

        self._view.update_page()

    def _choiceAlbum(self, e):
        self._albumValue = e.control.data

    def handleSelezione(self,e):
        pass