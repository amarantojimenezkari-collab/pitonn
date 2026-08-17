"""
Proyecto Integrador — Motor Minimalista de Middlewares y Dispatcher de Eventos
Contexto: la columna vertebral de notificaciones de Joblify: cuando alguien
se postula a una vacante, se dispara un evento y varios listeners reaccionan
(mandar email, notificar al reclutador, guardar en log), todo desacoplado.
"""


class EventDispatcher:
    def __init__(self, detener_en_error=False):
        self.detener_en_error = detener_en_error
        self._listeners = {}  # {nombre_evento: [callback1, callback2, ...]}

    def registrar(self, nombre_evento, callback):
        """Guarda un callback asociado a un evento."""
        self._listeners.setdefault(nombre_evento, []).append(callback)

    def _limpiar_payload(self, payload):
        """Recorre el payload recursivamente y limpia espacios en los strings."""
        if isinstance(payload, str):
            return payload.strip()
        if isinstance(payload, dict):
            return {clave: self._limpiar_payload(valor) for clave, valor in payload.items()}
        if isinstance(payload, list):
            return [self._limpiar_payload(item) for item in payload]
        return payload

    def emitir(self, nombre_evento, **payload):
        payload_limpio = self._limpiar_payload(payload)
        listeners = self._listeners.get(nombre_evento, [])

        if not listeners:
            print(f"(sin listeners registrados para '{nombre_evento}')")
            return

        for callback in listeners:
            try:
                # Desempaquetado dinámico del payload como kwargs del callback
                callback(**payload_limpio)
            except Exception as error:
                print(f"Error en listener de '{nombre_evento}': {error}")
                if self.detener_en_error:
                    raise


def enviar_email_confirmacion(candidato, vacante, **_):
    print(f"[EMAIL] Confirmación enviada a {candidato} por postularse a '{vacante}'")


def notificar_reclutador(candidato, vacante, **_):
    print(f"[NOTIFICACION] Reclutador avisado: {candidato} aplicó a '{vacante}'")


def guardar_en_bitacora(**payload):
    print(f"[LOG] {payload}")


if __name__ == "__main__":
    dispatcher = EventDispatcher(detener_en_error=False)

    dispatcher.registrar("postulacion_creada", enviar_email_confirmacion)
    dispatcher.registrar("postulacion_creada", notificar_reclutador)
    dispatcher.registrar("postulacion_creada", guardar_en_bitacora)

    dispatcher.emitir(
        "postulacion_creada",
        candidato="  Karla Ríos  ",       # con espacios de sobra a propósito
        vacante="  Backend Developer  ",  # para probar la limpieza recursiva
    )

    dispatcher.emitir("vacante_cerrada", vacante="Backend Developer")
