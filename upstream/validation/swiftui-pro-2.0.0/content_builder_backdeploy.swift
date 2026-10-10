import SwiftUI
struct Card<Content: View>: View {
 @ContentBuilder var content: Content
 var body: some View { content }
}
struct Sample: View { var body: some View { Card { Text("A"); Text("B") } } }
