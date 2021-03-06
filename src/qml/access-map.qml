import QtQuick 2.11
import QtPositioning 5.11
import QtLocation 5.11

Rectangle {
    id:rectangle
    width: 720
    height: 480
    Plugin {
        id: osmPlugin
        name: "osm"
    }

    Map {
        id: map
        anchors.fill: parent
        plugin: osmPlugin
        center: QtPositioning.coordinate(38.246473, 21.734790)
        zoomLevel: 20
        
        MapItemView{
            model: markermodel
            delegate: MapQuickItem {
                coordinate: model.position_marker
                anchorPoint.x: image.width
                anchorPoint.y: image.height
                sourceItem:
                    Image { id: image; source: model.source_marker }
            }
        }
    }
}