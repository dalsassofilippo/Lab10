from asyncio import set_event_loop

import flet as ft

from database.DAO import DAO


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleCalcola(self, e):
        self._view._txt_result.clean()
        if self._view._txtAnno.value=="":
            self._view.create_alert("Attenzione: inserire l'anno!")
            self._view.update_page()
            return
        anno =int(self._view._txtAnno.value)
        if anno<1816 or anno>2016:
            self._view.create_alert("Attenzione: anno fuori dai parametri di ricerca!")
            self._view.update_page()
            return

        self._model.crea_grafo(anno)

        country = DAO.getAllNodes(anno)# Call the method
        for i in range(len(country)):
            self._view._ddStato.options.append(ft.dropdown.Option(key=country[i].CCode, text=country[i].__str__()))

        if self._model.getIdMap() is None:
            self._view.create_alert("Errore nella creazione del grafo!")
            self._view.update_page()
            return
        else:
            self._view._txt_result.controls.append(ft.Text("Grafo correttamente creato.", color="green"))
            self._view._txt_result.controls.append(ft.Text(f"Il grafo ha {self._model.getNumConnected()} componenti connesse."))
            self._view._txt_result.controls.append(ft.Text("Di seguito i dettagli sui nodi:"))
            for nodo in self._model.getIdMap():
                self._view._txt_result.controls.append(ft.Text(f"{self._model.getCoutry(nodo)} -- {self._model.getNeighbour(self._model.getCoutry(nodo))} vicini."))
            self._view.update_page()
            return

    def handleRaggiungibili(self,e):

        if self._view._ddStato.value is None:
            self._view.create_alert("Attenzione: selezionare stato!")
            self._view.update_page()
            return
        stato = self._model.getCoutry(int(self._view._ddStato.value))

        raggiungibili=self._model.statiRaggiungibili(stato)

        if len(raggiungibili)==1:
            self._view.create_alert("Ops, nessuno stato raggiungibile :)")
            self._view.update_page()
            return
        self._view._txt_result.clean()

        for c in raggiungibili:
            self._view._txt_result.controls.append(ft.Text("Nodi raggiungibili correttamente trovati.", color="green"))
            self._view._txt_result.controls.append(ft.Text(f"Nodo di partenza: {stato.__str__()}; può raggiungere {len(raggiungibili)} stati."))
            self._view._txt_result.controls.append(ft.Text("Di seguito la lista:"))
            for s in range(1,len(raggiungibili)):
                self._view._txt_result.controls.append(ft.Text(
                    f"{raggiungibili[s].__str__()}"))

        self._view.update_page()








