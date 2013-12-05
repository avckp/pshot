#/usr/bin/python2
import os
import time
import cairo
import thread
from gi.repository import Gtk, GdkPixbuf


class take_screenshot_at_launch:
    width = os.system("xdpyinfo | grep dimensions | awk '{print $2}' | awk -Fx '{print $1}'")
    height = os.system("xdpyinfo | grep dimensions | awk '{print $2}' | awk -Fx '{print $2}'")
    os.system('imlib2_grab -width 425 -height 240 /tmp/Screenshot2.png')
    os.system('imlib2_grab -width "{0}" -height "{1}" /tmp/Screenshot1.png'.format(width, height))
take_screenshot_at_launch()


class sceenshot_gui:

    def draw_transparency(self, widget, cr):
        cr.set_source_rgba(.1, .1, .1, 0.6)
        cr.set_operator(cairo.OPERATOR_SOURCE)
        cr.paint()
        cr.set_operator(cairo.OPERATOR_OVER)

    def on_take_new_snapshot_clicked(self, widget):
        time.sleep(float(self.capture_delay_button.get_text()))

        if self.capturemode.get_active_text() == "Custom Width & Height":
            try:
                os.system('imlib2_grab -width {0} -height {1} /tmp/Screenshot1.png'.format(int(self.snapshot_width.get_text()), int(self.snapshot_height.get_text())))
                os.system('imlib2_grab -width 425 -height 240 /tmp/Screenshot2.png')
                self.PNG.set_from_file('/tmp/Screenshot2.png')
            except ValueError:
                dialog_detected_letters = Gtk.MessageDialog(None, 0, Gtk.MessageType.WARNING,
                Gtk.ButtonsType.OK, "Type only numbers, please !")
                dialog_detected_letters.format_secondary_text("")
                dialog_detected_letters.run()
                dialog_detected_letters.destroy()

        if self.capturemode.get_active_text() == "Full Screen":
            width = os.system("xdpyinfo | grep dimensions | awk '{print $2}' | awk -Fx '{print $1}'")
            height = os.system("xdpyinfo | grep dimensions | awk '{print $2}' | awk -Fx '{print $2}'")
            os.system('imlib2_grab -width "{0}" -height "{1}" /tmp/Screenshot1.png'.format(width, height))
            os.system('imlib2_grab -width 425 -height 240 /tmp/Screenshot2.png')
            self.PNG.set_from_file('/tmp/Screenshot2.png')

    def on_save_as_clicked(self, widget):
        chooser_dialog = Gtk.FileChooserDialog(title="Save To..."
        ,action=Gtk.FileChooserAction.SAVE
        ,buttons=["Save", Gtk.ResponseType.ACCEPT, "Cancel", Gtk.ResponseType.CANCEL])
        response = chooser_dialog.run()
        filename = chooser_dialog.get_filename()

        if response == Gtk.ResponseType.ACCEPT:
            if filename.endswith(".jpeg"):
                os.system("convert /tmp/Screenshot1.png '{0}'".format(filename))
            elif filename.endswith(".png"):
                os.system("cp /tmp/Screenshot1.png " + filename)
            elif filename.endswith(".jpg"):
                os.system("convert /tmp/Screenshot1.png '{0}'".format(filename))
            elif filename.endswith(".bmp"):
                os.system("convert /tmp/Screenshot1.png '{0}'".format(filename))
            elif filename.endswith(".tiff"):
                os.system("convert /tmp/Screenshot1.png '{0}'".format(filename))
            elif filename.endswith(".tif"):
                os.system("convert /tmp/Screenshot1.png '{0}'".format(filename))
            else:
                os.system("cp /tmp/Screenshot1.png " + filename + ".png")
        if response == Gtk.ResponseType.CANCEL:
            pass
        chooser_dialog.destroy()

    def on_about_clicked(self, widget):
        aboutdialog = Gtk.AboutDialog()
        aboutdialog.set_program_name("Pshot")
        aboutdialog.set_logo(GdkPixbuf.Pixbuf.new_from_file("data_pshot/pshot_logo.png"))
        aboutdialog.set_comments("Screenshot Utility\n")
        aboutdialog.set_website("http://linux.sytes.net/")
        aboutdialog.set_website_label("Developer Website")
        aboutdialog.set_authors(["Aaron"])
        aboutdialog.set_license('GPLv3 - http://www.gnu.org/licenses/gpl.html')
        aboutdialog.run()
        aboutdialog.destroy()

    def thread_gimp(self, widget):
        os.system("gimp /tmp/Screenshot1.png")

    def on_send_to_gimp_clicked(self, widget):        
        thread.start_new_thread(self.thread_gimp, ("start_gimp_in_new_thread", ))

    def __init__(self):
        self.intf = Gtk.Builder()
        self.intf.add_from_file('data_pshot/pshot.glade')
        self.intf.connect_signals(self)
        self.capturemode = self.intf.get_object('capturemodebox')
        self.capturemode.set_active(0)
        self.PNG = self.intf.get_object("image1")
        self.PNG.set_from_file('/tmp/Screenshot2.png')
        self.capture_delay_button = self.intf.get_object('spinbutton1')
        self.snapshot_height = self.intf.get_object('snapshot_height')
        self.snapshot_width = self.intf.get_object('snapshot_width')
        self.capturemode = self.intf.get_object('capturemodebox')
        self.window = self.intf.get_object("window1")
        self.window.screen = self.window.get_screen()
        self.window.visual = self.window.screen.get_rgba_visual()
        if self.window.visual != None and self.window.screen.is_composited():
            self.window.set_visual(self.window.visual)
        self.window.set_app_paintable(True)
        self.window.connect("draw", self.draw_transparency)
        self.window.connect("delete-event", Gtk.main_quit)
        self.window.show_all()

if __name__ == '__main__':
    sceenshot_gui()
    Gtk.main()