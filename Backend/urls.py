from django.urls import path
from Backend import views


urlpatterns = [

    path('Index_page/',views.Index_page,name="Index_page"),


    path('Login_admin/',views.Login_admin,name="Login_admin"),
    path('adminuser/',views.adminuser,name="adminuser"),
    path('admin_logout/',views.admin_logout,name="admin_logout"),


    path('Add_Flight/',views.Add_Flight,name="Add_Flight"),
    path('flightdata/',views.flightdata,name="flightdata"),
    path('Display_Flight/',views.Display_Flight,name="Display_Flight"),


    path('TourPackageAdd/',views.TourPackageAdd,name="TourPackageAdd"),
    path('contactusdisplay/',views.contactusdisplay,name="contactusdisplay"),
    path('contactusdelete/<int:data_id>/',views.contactusdelete,name="contactusdelete"),


    path('TourPackageDisplay/',views.TourPackageDisplay,name="TourPackageDisplay"),
    path('TourPackageReply/',views.TourPackageReply,name="TourPackageReply"),
    path('tourpackagedata/',views.tourpackagedata,name="tourpackagedata"),
    path('TourPackageDelete/<int:data_id>/',views.TourPackageDelete,name="TourPackageDelete"),
    path('TourPackageReplyDelete/<int:data_id>/',views.TourPackageReplyDelete,name="TourPackageReplyDelete"),
    path('TourPackageEdit/<int:tour_id>/',views.TourPackageEdit,name="TourPackageEdit"),
    path('TourPackageUpadate/<int:tour_id>/',views.TourPackageUpadate,name="TourPackageUpadate"),



    path('Delete_Flight/<int:data_id>/',views.Delete_Flight,name="Delete_Flight"),
    path('Edit_Flight/<int:dataid>/',views.Edit_Flight,name="Edit_Flight"),
    path('Update_Flight/<int:dataid>/',views.Update_Flight,name="Update_Flight"),


    path('explore_hotel/',views.explore_hotel,name="explore_hotel"),
    path('exploredata/',views.exploredata,name="exploredata"),
    path('expolre_display/',views.expolre_display,name="expolre_display"),
    path('explore_delete/<int:exp_id>/',views.explore_delete,name="explore_delete"),
    path('explore_edit/<int:exp_id>/',views.explore_edit,name="explore_edit"),
    path('explore_update/<int:explo_id>/',views.explore_update,name="explore_update"),

    path('HotelRoomCatagory/',views.HotelRoomCatagory,name="HotelRoomCatagory"),
    path('hotel_room_cat/',views.hotel_room_cat,name="hotel_room_cat"),
    path('Hotel_RoomCat_Display/',views.Hotel_RoomCat_Display,name="Hotel_RoomCat_Display"),
    path('delete_roomCat/<int:del_id>/',views.delete_roomCat,name="delete_roomCat"),
    path('edit_roomCat/<int:cat_id>/',views.edit_roomCat,name="edit_roomCat"),
    path('Update_RoomCat/<int:Cat_id>/',views.Update_RoomCat,name="Update_RoomCat"),

    path('hotel_room_add/',views.hotel_room_add,name="hotel_room_add"),
    path('roomdata/',views.roomdata,name="roomdata"),
    path('room_display/',views.room_display,name="room_display"),
    path('room_edit/<int:pro_id>/',views.room_edit,name="room_edit"),
    path('Update_Room/<int:pro_id>/',views.Update_Room,name="Update_Room"),
    path('room_delete/<int:del_id>/',views.room_delete,name="room_delete"),

    ]