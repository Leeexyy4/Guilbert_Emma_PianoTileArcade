import pygame
from ui.page.basePage import BasePage
from ui.utils.inputBox import InputBox

class ConnexionPage(BasePage):
    def affichagePage(self):
        window = self._windowManager.getWindow()
        font = self._windowManager.getFontSmall()
        font_title = self._windowManager.getFontTall()
        color = self._windowManager.getColor()
        blanc = color.getBlanc()
        violet = color.getViolet()
        noir = (0, 0, 0)

        screen_width = self._windowManager.getScreenWidth()
        screen_height = self._windowManager.getScreenHeight()

        form_width = 400
        form_height = 300
        form_x = (screen_width - form_width) // 2
        form_y = (screen_height - form_height) // 2

        pygame.draw.rect(window, color.getGris(), (form_x - 20, form_y - 40, form_width + 40, form_height + 100))

        titre = font_title.render("Connexion", True, noir)
        window.blit(titre, titre.get_rect(center=(screen_width // 2, form_y + 10)))

        spacing = 100
        input_x = form_x + (form_width - 280) // 2
        input_y = form_y

        # Libellés + champs
        labels = ["Nom d'utilisateur :", "Mot de passe :"]
        inputs = [self.input_username, self.input_password]

        for i in range(2):
            label = font.render(labels[i], True, noir)
            window.blit(label, (input_x, input_y + 60 + i * spacing))
            inputs[i].rect.topleft = (input_x, input_y + 100 + i * spacing)
            inputs[i].draw(window)

        self.button_valider.topleft = (input_x, input_y + 80 + 2 * spacing)
        pygame.draw.rect(window, violet, self.button_valider)
        txt = font.render("Valider", True, blanc)
        window.blit(txt, txt.get_rect(center=self.button_valider.center))

        if self.erreur_connexion:
            erreur_texte = font.render("Identifiants incorrects", True, (255, 0, 0))
            window.blit(erreur_texte, (input_x, input_y + 80 + 3 * spacing))


    def handle_event(self, event):
        self.input_username.handle_event(event)
        self.input_password.handle_event(event)
        self._windowManager.getInterface().setUpdate(True)